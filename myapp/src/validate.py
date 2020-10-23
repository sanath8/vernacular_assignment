from typing import List, Dict, Callable, Tuple
SlotValidationResult = Tuple[bool, bool, str, Dict]


class Validate:
    """
    Base class for finite set and numerical value validation sub classes.
    """
    def __init__(self):
        """
        Initialize the output fields
        """
        self.filled           = True
        self.part_filled      = False
        self.trigger          = ''
        self.parameters       = {}
    
    def set_filled(self, val: bool) -> None:
        """
        Setter method filled field
        """
        self.filled = val

    def set_part_filled(self, val: bool) -> None:
        """
        Setter method for partially filled field
        """
        self.part_filled = val

    def set_trigger(self, val: str) -> None:
        """
        Setter method for invalid trigger field
        """
        self.trigger = val

    def set_parameters(self, values: List[str], key: str, support_multiple: bool = True, pick_first: bool = False) -> None:
        """
        Setter method for valid values field
        In case both support_multiple and pick_first are set to true or false, support_multiple will be prioritized.
        """
        if values != []:
            if support_multiple or (not support_multiple and not pick_first):
                self.parameters = {key : values} # If support_multiple is true, list of all valid values are sent in response
            else:
                self.parameters = {key : str(values[0])} # If pick_first is true, the first valid value is sent as a string in response

    def get_filled(self) -> bool:
        """
        Getter method for filled field
        """
        return self.filled

    def get_part_filled(self) -> bool:
        """
        Getter method for partially filled field
        """
        return self.part_filled

    def get_trigger(self) -> str:
        """
        Getter method for invalid trigger field
        """
        return self.trigger

    def get_parameters(self) -> Dict:
        """
        Getter method for valid values
        """
        return self.parameters


    def get_response(self) -> SlotValidationResult:
        """
        The response to be sent as per the given format
        """
        return (
	        self.get_filled(),
                self.get_part_filled(),
                self.get_trigger(),
                self.get_parameters()
                )

