from pathlib import Path

project_root_dir = Path(__file__).parent.joinpath('..', '..').resolve()

assets_dir = project_root_dir.joinpath('assets')
glyphs_dir = assets_dir.joinpath('glyphs')
templates_dir = assets_dir.joinpath('templates')
images_dir = assets_dir.joinpath('images')
www_static_dir = assets_dir.joinpath('www-static')

build_dir = project_root_dir.joinpath('build')
outputs_dir = build_dir.joinpath('outputs')
releases_dir = build_dir.joinpath('releases')
www_dir = build_dir.joinpath('www')

docs_dir = project_root_dir.joinpath('docs')
