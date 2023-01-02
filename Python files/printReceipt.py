from sh import lp
from settings import receiptFile,printername

def printReceipt():
    lp_cp = lp.bake('-d')
    lp_cp (printername, receiptFile)

if __name__ == '__main__':
    main()

