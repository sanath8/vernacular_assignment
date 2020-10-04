from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


class Validate:
    def __init__(self):
        self.filled           = True
        self.part_filled      = False
        self.trigger          = ''
        self.parameters       = {}
    
    def set_filled(self, val: bool) -> None:
        self.filled = val

    def set_part_filled(self, val: bool) -> None:
        self.part_filled = val

    def set_trigger(self, val: str) -> None:
        self.trigger = val

    def set_parameters(self, values: List[str], key: str, support_multiple: bool = True, pick_first: bool = False) -> None:
        """
        In case both support_multiple and pick_first are set to true or false, support_multiple will be prioritized.
        """
        if values != []:
            if support_multiple or (not support_multiple and not pick_first):
                self.parameters = {key : values}
            else:
                self.parameters = {key : values[0]}



    def get_response(self) -> SlotValidationResult:
        return {
                    "filled" : self.filled,
                    "partially_filled" : self.part_filled,
                    "trigger" : self.trigger,
                    "parameters" : self.parameters
                }

