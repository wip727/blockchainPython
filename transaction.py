class Transaction(object):
    # define transaction input and output metaclass
    class Input():
        def __init__(self, prevTxHash, outputIndex):
            self.prevTxHash = prevTxHash            
            self.outputIndex = outputIndex
            self.signature = []

        def addSignature(sig):
            if sig:
                self.signature = sig 
            else:
                print("Signature error!")

            return self.signature

    class Output():
        def __init__(self, value, address):
            self.value = value
            self.address = address

    def __init__(self):
        self.inputs = []
        self.outputs = []
        self.hash = str.encode("")

    def getRawDataToSign(index):
        if index > len(self.inputs):
            return

        sigData = []
        inputToSign = self.inputs[index]
        prevTxHash = inputToSign.prevTxHash
        outputIndex = inputToSign.outputIndex
        outputs = self.outputs

        if prevTxHash:
            for char in prevTxHash:
                sigData.append(char)

        if outputIndex:
            for index in outputIndex:
                sigData.append(index)

        if outputs:
            for output in outputs:
                for v in output.value:
                    sigData.append(v)
                for char in output.address:
                    sigData.append(char)

        # TO DO: byte array operation?

        return sigData

    # TO DO: getRawTx
    # TO DO: finalize

    def setHash(h):
        self.hash = h

    def getHash():
        return self.hash

    # Transaction input/output setters and getters

    def addInput(prevTxHash, outputIndex):
        txInput = Input(prevTxHash, outputIndex)
        self.inputs.append(txInput)

    def addOutput(value, address):
        txOutput = Output(value, address)
        self.outputs.append(txOutput)

    def removeInput(index):
        del self.inputs[index]

    # TO DO: removeInput by UTXO ut

    def getInputs():
        return self.inputs

    def getOutputs():
        return self.outputs

    def getInput(index):
        if index < len(self.inputs):
            return self.inputs[index]

        return None

    def getOutput(index):
        if index < len(self.outputs):
            return self.outputs[index]

        return None

    def numInputs():
        return len(self.inputs)

    def numOutputs():
        return len(self.outputs)


