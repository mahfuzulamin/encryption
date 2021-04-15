from pathlib import Path
from typing import List, Optional, Union
 
import typer
 
from .hexadecimal import Hexadecimal
 
def encryption_app() -> typer.Typer:
    
    app = typer.Typer()
    
    @app.command()
    def hex(args: List[str]) -> None:
        hex = Hexadecimal(args[1])
        print(f"list is {args}.")
        encodedMsg = ""
        if args[0] == 'encode':
            encodedMsg = hex.encode()
        elif args[0] == 'decode':
            encodedMsg = hex.decode()

        print(f"Hex {args[0]} message is {encodedMsg}.")

    @app.command()
    def atbash(message: str) -> None:
        hex = Hexadecimal(message)
        encodedMsg = hex.encode()
        print(f"Hex encoded message is {encodedMsg}.")

    return app 