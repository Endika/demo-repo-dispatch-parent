.PHONY: all clean

all:
	@echo "🔨 Generating service files..."
	python scripts/generator.py
	@echo "✅ Generation complete!"

clean:
	@echo "🧹 Cleaning up generated files..."
	rm -rf dist
	@echo "✅ Cleanup complete!"
