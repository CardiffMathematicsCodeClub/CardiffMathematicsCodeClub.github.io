#!/bin/bash

# Get the latest tags
git fetch upstream --tags

# Get the latest version in the form x.y
ver=$(git tag | tail -n 1 | sed 's/v//')

# Get the x part of the version
major_ver=$(echo $ver | sed 's/\.[0-9]*//')

# Get the y part of the version
minor_ver=$(echo $ver | sed 's/[0-9]*\.//')

# Calculate the number of commits since the last release for the patch version (z)
patch_ver=$[ $(git log $(git tag | tail -n 1)..HEAD --pretty=oneline | wc -l) + 1]

# Put it all together
version="${major_ver}.${minor_ver}.${patch_ver}"

# Tell the user
echo "Bumped to version v$version"

# Finally find and replace in the _config.yml file
sed -i -- "s/\(version: \)[0-9]*\.[0-9]*\.[0-9]*/\1${version}/" _config.yml

# One last thing, add the changes to the commit
git add _config.yml

