build:
	maturin build --release

release:
	twine upload target/wheels/graphemex