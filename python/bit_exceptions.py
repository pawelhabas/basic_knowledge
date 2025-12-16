#   User defined Exception
class BITException(Exception):

    def __init__(self, text, area):
        super().__init__(text)
        self.area = area

    def __str__(self):
        return "{}, area: {}".format(super().__str__(), self.area)


class BITSecurityException(BITException):
    pass

class BITDataFormatException(BITException):
    pass

##############

try:
    1/0

except BITSecurityException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
    print("Application error: {}".format(e))
except Exception as e:
    print("General error: {}".format(e))
finally:
    print("-*- " * 8)

try:
    raise BITSecurityException("Access denied: insufficient permissions to read the file.", "HR data")

except BITSecurityException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
    print("Application error: {}".format(e))
except Exception as e:
    print("General error: {}".format(e))
finally:
    print("-*- " * 8)

try:
    raise BITDataFormatException("Not acceptable file type", "PR data")

except BITSecurityException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
    print("Application error: {}".format(e))
except Exception as e:
    print("General error: {}".format(e))
finally:
    print("-*- " * 8)
try:
    raise BITException("File format is incorrect", "Financial data")

except BITSecurityException as e:
    print("Application security error: {}".format(e))
except BITDataFormatException as e:
    print("Application data malformed error: {}".format(e))
except BITException as e:
    print("Application error: {}".format(e))
except Exception as e:
    print("General error: {}".format(e))
finally:
    print("-*- " * 8)