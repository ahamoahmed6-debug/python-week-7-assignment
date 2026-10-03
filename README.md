# PLP Python Week 7 - Shopping List Manager

## File Descriptions
* `list_warmup.py`: Demonstrates basic list mutations using index selection, element injection via `.append()`, removal with `.remove()`, and tracking metrics via `len()`.
* `shopping_list.py`: A runtime interactive command-line interface that allows manual addition, safe conditional extraction, and viewing of standard collection strings.
* `list_report.py`: Iterates structurally over a list of items to sort length attributes, count instances matching string length filters, and manually isolate the longest element index.

## Reflection Question
It is safer to check membership using the `in` operator before calling `.remove()` because attempting to remove an item that does not exist in a Python list immediately causes a `ValueError` runtime crash. By verifying the element is present beforehand, the application can handle the missing entry smoothly using control flow instructions (`if/else`) without breaking the execution flow of the entire application.
