"""Script to produce additional metrics for Prometheus"""
# pylint: disable=wrong-import-position
import os                                                               # noqa:E402,E501
from prometheus_fastapi_instrumentator import Instrumentator, metrics   # noqa:E402,E501
# pylint: enable=wrong-import-position


NAMESPACE = os.environ.get("METRICS_NAMESPACE", "fastapi")
SUBSYSTEM = os.environ.get("METRICS_SUBSYSTEM", "model")

instrumentator = Instrumentator(
    should_group_status_codes=True,
    should_ignore_untemplated=True,
    should_instrument_requests_inprogress=True,
    excluded_handlers=["/metrics"],
    inprogress_name="fastapi_inprogress",
    inprogress_labels=True,
)

# Additional Prometheus Default Metrics

instrumentator.add(
    metrics.request_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="musicexpress_request_size",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
).add(
    metrics.response_size(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="musicexpress_response_size",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
).add(
    metrics.latency(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="musicexpress_latency",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
).add(
    metrics.requests(
        should_include_handler=True,
        should_include_method=True,
        should_include_status=True,
        metric_name="musicexpress_no_requests",
        metric_namespace=NAMESPACE,
        metric_subsystem=SUBSYSTEM,
    )
)
