import argparse

def main():
    parser = argparse.ArgumentParser(description="A simple CLI example.")
    parser.add_argument("name", help="Your name")
    parser.add_argument("--greet", action="store_true", help="Say hello")

    args = parser.parse_args()

    if args.greet:
        print(f"Hello, {args.name}!")
    else:
        print(f"Name entered: {args.name}")

if __name__ == "__main__":
    main()

import click

@click.command()
@click.argument('name')
@click.option('--greet', is_flag=True, help='Say hello')
def cli(name, greet):
    if greet:
        click.echo(f"Hello, {name}!")
    else:
        click.echo(f"Name entered: {name}")

if __name__ == "__main__":
    cli()
