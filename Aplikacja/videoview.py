import logging

from PyQt5.QtWidgets import (
    QGraphicsRectItem,
    QGraphicsScene,
    QGraphicsSceneMouseEvent,
    QGraphicsView,
)
from PyQt5.QtGui import (
    QPainter,
    QPen,
    QColor,
    QResizeEvent,
)
from PyQt5.QtCore import (
    QLineF,
    QPointF,
    QRect,
    QRectF,
    QSizeF,
    Qt,
    pyqtSignal as Signal,
)
from PyQt5.QtMultimediaWidgets import QGraphicsVideoItem


class VideoScene(QGraphicsScene):
    regionSelected = Signal(QRect)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.videoItem = QGraphicsVideoItem()
        self.videoItem.setPos(0, 0)
        self.videoItem.nativeSizeChanged.connect(self.videoSizeChanged)
        self.addItem(self.videoItem)

        self.rectangle = QGraphicsRectItem()
        self.rectangle.setPen(QColor(0, 122, 217))
        self.addItem(self.rectangle)

    def videoSizeChanged(self, size: QSizeF):
        logging.debug("%s", size)
        if not size.isEmpty():
            self.videoItem.setSize(size)
            self.setSceneRect(self.videoItem.boundingRect())
            self.clearSelection()

    def clearSelection(self) -> None:
        self.rectangle.setRect(QRectF())
        self.regionSelected.emit(self.selection)

    @property
    def selection(self) -> QRect:
        return self.rectangle.rect().toRect()

    @staticmethod
    def coerceInside(point: QPointF, rect: QRectF):
        return QPointF(
            min(max(point.x(), rect.left()), rect.right()),
            min(max(point.y(), rect.top()), rect.bottom()),
        )

    def coerceInsideVideo(self, point: QPointF):
        return self.coerceInside(point, self.videoItem.boundingRect())

    def mousePressEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        self.startPos = self.coerceInsideVideo(event.scenePos())
        return super().mousePressEvent(event)

    def mouseMoveEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        endPos = self.coerceInsideVideo(event.scenePos())
        self.rectangle.setRect(QRectF(self.startPos, endPos).normalized())
        return super().mouseMoveEvent(event)

    def mouseReleaseEvent(self, event: QGraphicsSceneMouseEvent) -> None:
        logging.info("Selection: %s", self.selection)
        super().mouseReleaseEvent(event)
        self.regionSelected.emit(self.selection)

    def paintGrid(self, painter: QPainter, rect: QRectF, gridSize: int):
        left, top, right, bottom = rect.getCoords()
        x_min = (int(left - 1) // gridSize + 1) * gridSize
        y_min = (int(top - 1) // gridSize + 1) * gridSize
        x_max = (int(right) // gridSize) * gridSize
        y_max = (int(bottom) // gridSize) * gridSize
        # logging.debug(
        #     "x=(%s<=%s..%s<=%s) y=(%s<=%s..%s<=%s)",
        #     *(left, x_min, x_max, right),
        #     *(top, y_min, y_max, bottom)
        # )
        painter.setPen(QPen(Qt.gray, 2))
        painter.drawLines(QLineF(0, top, 0, bottom), QLineF(left, 0, right, 0))
        painter.setPen(QPen(Qt.gray, 1))
        painter.drawLines(
            QLineF(x, top, x, bottom) for x in range(x_min, x_max + 1, gridSize) if x
        )
        painter.drawLines(
            QLineF(left, y, right, y) for y in range(y_min, y_max + 1, gridSize) if y
        )

    def drawBackground(self, painter: QPainter, rect: QRectF) -> None:
        super().drawBackground(painter, rect)
        self.paintGrid(painter, rect, 20)


class VideoView(QGraphicsView):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        scene = VideoScene(self)
        self.setScene(scene)
        scene.sceneRectChanged.connect(self.sceneRectChanged)

    def scene(self) -> VideoScene:
        return super().scene()

    def _zoomToVideo(self):
        if not self.scene().videoItem.nativeSize().isEmpty():
            self.fitInView(self.scene().videoItem, Qt.KeepAspectRatio)

    def sceneRectChanged(self, rect: QRectF) -> None:
        self._zoomToVideo()

    def resizeEvent(self, event: QResizeEvent) -> None:
        super().resizeEvent(event)
        self._zoomToVideo()