from hamcrest.core.base_matcher import BaseMatcher
from hamcrest.core.helpers.hasmethod import hasmethod


class AllOperations(BaseMatcher):

    def __init__(self, operations):
        self.operations = operations
        self.missing = None

    def _matches(self, item):
    	return not (False in [o in str(item) for o in self.operations])

    def describe_to(self, description):
        description.append_text('Operations should contain all of: ')    \
                   .append_text(self.operations)

def all_operations():
    return AllOperations('+-*/')