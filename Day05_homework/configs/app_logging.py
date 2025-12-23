import logging

from colorlog import ColoredFormatter

from configs.trace import trace_id_ctx


class TraceIdFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        record.trace_id = trace_id_ctx.get() or "n/a"
        return True


# Gọi 1 lần khi app start để
# tạo formatter có %(trace_id)s
# và gắn TraceIdFilter vào root logger
def setup_logging(sql_echo: bool = False) -> None:
    root = logging.getLogger()
    root.setLevel(logging.INFO)

    trace_filter = TraceIdFilter()

    formatter = ColoredFormatter(
        fmt="%(log_color)s %(asctime)s %(levelname)s "
        "[trace_id=%(trace_id)s] %(name)s: %(message)s",
        log_colors={
            "DEBUG": "white",
            "INFO": "blue",
            "WARNING": "yellow",
            "ERROR": "red",
            "CRITICAL": "bold_red",
        },
    )

    if root.handlers:
        for h in root.handlers:
            h.addFilter(trace_filter)
            h.setFormatter(formatter)
    else:
        handler = logging.StreamHandler()
        handler.setFormatter(formatter)
        handler.addFilter(trace_filter)
        root.addHandler(handler)

    sa_logger = logging.getLogger("sqlalchemy.engine")
    sa_logger.setLevel(logging.INFO if sql_echo else logging.WARNING)
    sa_logger.propagate = True
