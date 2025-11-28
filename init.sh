#!/bin/bash
read -p "Enter project name (snake_case): " name

# Rename folder
git mv src/project_name "src/$name"

sed -i '' "s/project_name/$name/g" pyproject.toml
sed -i '' "s/project_name/${name//_/-}/g" pyproject.toml

rm -rf .git
git add .
git commit -m "chore: initialize project"

echo "Project initialized as: $name"
echo "Run 'poetry install' to complete setup"