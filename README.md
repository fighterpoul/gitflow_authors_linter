# About

gitflow_authors_linter is an official plugin for [gitflow_linter]() command line tool.
The plugin checks if currently a single author does not have too many open, ongoing feature branches. 
Having multiple open feature branches by a single author might be an indicator that something is wrong with the process. On top of that merging all those branches might be complex in a near future.

# Quick Start

## Installation

You can install the linter from

* pip

```
pip install gitflow-linter-authors
```

* or the source code

```
git clone https://github.com/fighterpoul/gitflow_authors_linter.git
cd gitflow_authors_linter
git checkout 0.0.1
python setup.py install
```

## Usages

All you need to do is to: 

1. Add new item in your YAML file that configures how `gitflow-linter` should work:

```yaml
rules:
  no_multiple_open_features_per_author:
    max_open_branches_per_author: 4 # mandatory
```

2. Run `gitflow-linter` - it should automatically recognize that the plugin must be used to check the given rule

# Motivation

The plugin is there for the two reasons:
1. Demonstrate how you may extend `gitflow-linter` by using plugins
1. Provide an additional step that verifies a given repository against authors

Therefore, it is supposed to be at the same time useful and educative.