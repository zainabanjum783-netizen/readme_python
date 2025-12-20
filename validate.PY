# Q7. Value Validator (hard)
# Write a function:

# def validate(value, *rules, allow_none=False, **options):

# Where:
# rules may include 'even', 'positive', 'integer'
# options may include:
# min=10
# max=100
# Return:
# "Valid"
# or an error message like "Value must be even"

def validate(value,*rule1,allow_none=False,**rule2):
    def limit1():
        for item in rule1:
            if('even'==item):
                if not(value%2==0):
                    return 'value must be even'
            if ('positive'==item):
                if (value<0):
                    return 'value must be positive'
            if ('integer'==item):
                if not(isinstance(value,int)):
                    return 'value must be integter'
    def none():
        if(allow_none==True):
            if not(value is None):
                return 'value is not none'
    def limit2():
        for keys in rule2.keys():
            if ('max'==keys):
                if value>rule2['max']:
                    return 'value is more than the max value'
            if ('min'==keys):
                if value<rule2['min']:
                    return 'value is less than the min value'
            
    if (limit1()==None and none()==None and limit2()==None):
        return 'valid'
    
# print(validate(24,'even','integer',max=50))
print(validate(None))
     
    