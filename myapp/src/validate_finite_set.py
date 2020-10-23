from .validate import *

class Validate_Finite_Set(Validate):
    """
    Subclass to validate if the values belong to a finite set and extract it
    """
    def validate_finite_values_entity(self, values: List[Dict], supported_values: List[str] = None,
                                invalid_trigger: str = None, key: str = None,
                                support_multiple: bool = True, pick_first: bool = False, **kwargs) -> SlotValidationResult:
        """
        Validate an entity on the basis of its value extracted.
        The method will check if the values extracted("values" arg) lies within the finite list of supported values(arg "supported_values").
    
        :param pick_first: Set to true if the first value is to be picked up
        :param support_multiple: Set to true if multiple utterances of an entity are supported
        :param values: Values extracted by NLU
        :param supported_values: List of supported values for the slot
        :param invalid_trigger: Trigger to use if the extracted value is not supported
        :param key: Dict key to use in the params returned
        :return: a tuple of (filled, partially_filled, trigger, params)
        """
        
        valid_values = [] # List to keep track of the valid values among the given values
       
        if not supported_values: # In case the value of supported_values is None
            supported_values = []

        if not values: # In case the values list is not passed in request
            values = []


        if len(values) == 0:
            self.set_trigger(invalid_trigger)
            self.set_filled(False)
            self.set_part_filled(False)
        else:
            supported_values_set = set(supported_values) # Set provides faster data acces.
            for each_value in values:
                if each_value["value"] in supported_values_set:
                    valid_values.append(each_value["value"].upper())
                else:
                    self.set_trigger(invalid_trigger)
                    self.set_filled(False)
                    self.set_part_filled(True)
                    valid_values = []
                    break
            self.set_parameters(valid_values, key, support_multiple, pick_first)
        
        return self.get_response() 

      

    
