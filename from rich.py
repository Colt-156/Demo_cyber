from rich.console import Console
from rich.table import Table

console = Console()

table = Table(show_header=True, header_style="bold magenta")
table.add_column("Name", style="dim", width=12)
table.add_column("Show in")
table.add_column("Rating", justify="right")
table.add_row(
    "Lilith", "Owl house", "8/10",
)
table.add_row(
    "Dipper",
    "[red]Gravity falls[/red]",
    "10/10",
)
table.add_row(
    "Fizzi",
    "Hevulla boss",
    "1000000/10",
)

console.print(table)