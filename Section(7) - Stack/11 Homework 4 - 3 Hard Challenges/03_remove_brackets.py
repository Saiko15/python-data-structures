
'''
Note: Code has no relation to infix/prefix/postfix conversions
It is important to not be trapped in something u know
Sometimes it is good to think in a very simple way without any complex tools u have

----------------------

Simple observation:
    Input: 					1-(2-3-(4+5-(6-7)))
    Remove all ( )			1-2-3-4+5-6-7
    Actual output:			1-2+3+4+5-6+7

    So every digit is just printed. Every sign, either as it is or flipped!

----------------------

In math, block will have a sign depends on parsing from the begin
We need to maintain what is the current sign for a block
Then with a sign and old sign we can decide the block sign
Image a block inside a block inside a block, etc
once a block is done, need to go back to our old status
stack can help us do that. This is a common pattern with stack
when u find things wish such recursive nature such as
 '''

def RemoveBrackets(str):
    # Assume single digits, unary

    def sign(a, b):			# How to mix 2 signs? E.g. -2(1-3)  ==> --3 = +3
        if a == b:
            return '+'  	# += 1 or  -= 1
        return '-'  		# +- or -+

    # for each new active block [e.g. from open (  ], we have new sign
    stk = ['+']		# current active sign for self block

    res = ""
    for idx, c in enumerate(str):
        if c.isdigit():
            res += c
        elif c == '+' or c == '-':
            res += sign(stk[-1], c)		# use current block sign with c to get sign
        elif c == '(' and stk: 			# block needs a sign: is it - or +? Use it with previous block sign
            if str[idx-1] != '(':		# case: -(5    so we use this - with the active sign
                stk.append(sign(stk[-1], str[idx - 1]))
            else:
                stk.append(stk[-1])		# case ((((: no change in sign. Just use last stack sign
        else:
            stk.pop()					# for  remove an active sign

    return res

if __name__ == '__main__':
    assert RemoveBrackets('1+2-3-4+5-6-7+8') == '1+2-3-4+5-6-7+8'
    assert RemoveBrackets('9-(2+3)') == '9-2-3'
    assert RemoveBrackets('9-(2-3)') == '9-2+3'
    assert RemoveBrackets('9+(2-3)') == '9+2-3'
    assert RemoveBrackets('1-(2-3-(4+5))-6-(7-8)') == '1-2+3+4+5-6-7+8'
    assert RemoveBrackets('1-(2-3-(4+5)+6-7)') == '1-2+3+4+5-6+7'
    assert RemoveBrackets('1-(2-3-(4+5-(6-7)))') == '1-2+3+4+5-6+7'
    assert RemoveBrackets('1-((4+5)-(6-7)))') == '1-4-5+6-7'
    assert RemoveBrackets('1-(((4-5)-(6-7))))') == '1-4+5+6-7'
    assert RemoveBrackets('1-(2-3-((4+5)-(6-7)))') == '1-2+3+4+5-6+7'
    assert RemoveBrackets('1-(2-3-((4-5)-(6-7)))') == '1-2+3+4-5-6+7'
    assert RemoveBrackets('1-(2-3+((4-5)-(6-7)))') == '1-2+3-4+5+6-7'
