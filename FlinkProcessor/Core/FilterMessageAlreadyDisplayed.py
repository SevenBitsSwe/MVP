from pyflink.datastream.functions import FilterFunction


class FilterMessageAlreadyDisplayed(FilterFunction):
    def open(self,runtime_context):
        pass

    def filter(self, value):
        return True