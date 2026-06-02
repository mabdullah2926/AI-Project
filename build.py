from pathlib import Path
import shutil


def main() -> None:
    project_root = Path(__file__).resolve().parent
    source = project_root / "frontend" / "index.html"
    target_dir = project_root / "public"
    target_dir.mkdir(exist_ok=True)
    shutil.copyfile(source, target_dir / "index.html")
    print("Copied frontend/index.html to public/index.html")


if __name__ == "__main__":
    main()

