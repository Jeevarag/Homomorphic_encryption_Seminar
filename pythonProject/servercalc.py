from linearmodel import LinModel
import phe as paillier
import json

from scipy.sparse import data


def getData():
	with open('data.json', 'r') as file:
		d=json.load(file)
	data=json.loads(d)
	return data


def computeData():
	data = getData()
	mycoef = LinModel().getCoef()
	pk = data['public_key']
	pubkey = paillier.PaillierPublicKey(n=int(pk['n']))

	# Extract ciphertexts and exponents from data
	encrypted_values = data['values']
	enc_nums_rec = [paillier.EncryptedNumber(pubkey, int(x[0]), int(x[1])) for x in encrypted_values]

	# Perform the computation
	results = sum([mycoef[i] * enc_nums_rec[i] for i in range(len(mycoef))])
	return results, pubkey
# print(computeData()[0].ciphertext())    #The calculated encrypted value(server side)
def serializeData():
	results, pubkey = computeData()
	encrypted_data={}
	encrypted_data['pubkey'] = {'n': pubkey.n}
	encrypted_data['values'] = (str(results.ciphertext()), results.exponent)
	serialized = json.dumps(encrypted_data)
	return serialized
# print(serializeData())				#Data to be sent to the customer side i.e. the calculated data along with public key
data = [45, 0, 1, 25.6, 130, 80, 105, 2]
mycoef = LinModel().getCoef()
print(sum([data[i]*mycoef[i] for i in range(len(data))]))
#
def main():
	datafile=serializeData()
	with open('answer.json', 'w') as file:
		json.dump(datafile, file)

if __name__=='__main__':
	main()