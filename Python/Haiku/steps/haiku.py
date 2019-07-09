from behave import *
from haiku_review import Haiku


@given(u'the haiku object has been created')
def step_impl(context):
    context.haiku = Haiku()
    pass


@when(u'i pass the string {string} to the the haiku review code')
def step_impl(context, string):
    try:
        context.result = context.haiku.haiku_checker(string)
    except ValueError:
        context.error = "Value"
        pass
    except TypeError:
        context.error = "Type"
        pass
    except Exception as err:
        raise AssertionError(f"Error raised: {err}")


@then(u'the output will confirm that it is a haiku')
def step_impl(context):
    assert context.result[3] == "Yes"


@then(u'the output will confirm that it is NOT a haiku')
def step_impl(context):
    assert context.result[3] == "No"


@step(u'the syllable counts for the lines will be 5, 7, 5 respectively')
def step_impl(context):
    assert context.result[0] == 5
    assert context.result[1] == 7
    assert context.result[2] == 5


@step(u'the syllable counts for the lines will be {syl} respectively')
def step_impl(context, syl):
    
    assert context.result[0] == eval(syl)[0]
    assert context.result[1] == eval(syl)[1]
    assert context.result[2] == eval(syl)[2]


@step(u'the code will throw a value error')
def step_impl(context):
    assert context.error == "Value"
  
  
@when(u'i pass the integer {integer} to the the haiku review code')
def step_impl(context, integer):
    try:
        value = int(integer)
        context.result = context.haiku.haiku_checker(value)
    except TypeError:
        context.error = "Type"
        pass
    except Exception as err:
        raise AssertionError(f"Error raised: {err}")
        
        
@step(u'the code will throw a type error')
def step_impl(context):
    assert context.error == "Type"

