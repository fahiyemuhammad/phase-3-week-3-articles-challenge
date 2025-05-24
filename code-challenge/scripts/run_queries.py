import sys
import os

# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

# Example queries
print("All Authors:")
for author in Author.all():
    print(f"- {author.name}")

print("\nAll Articles:")
for article in Article.all():
    print(f"- {article.title}")

print("\nAll Magazines:")
for mag in Magazine.all():
    print(f"- {mag.name} ({mag.category})")