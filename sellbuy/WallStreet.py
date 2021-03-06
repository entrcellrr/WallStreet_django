# Yash Bonde 28th September 2016
# This is the source file of the Wall Street Game that was conducted by the E-Cell of NIT Raipur
# in the annual techfest Aavartan, on 1st and 2nd October 2016.
# This is the third and most advanced iteration of the game Wall Street.
# This is a virtual share market game where, each person is given $10000 at the starting and
# the player with the maximum money in the end wins.

# Starting off with the basic input of the share price and amount of share prices
# The input of the current share price will be given in the function's input
# Shivaansh is handling the number of shares ... thingy
# this is the index at which the system wll be running, will be the input of the function

# Next we import all the packages that are required here
import numpy as np

# Regression data is here

'''

ACME (AME) : CocaCola :Misc
AmmunationPharma (APM) : PG: Pharma
BakerStreetFinding (BSF) : Bayry: Pharma
BajrangCafe (BJT) : TCS : Food
BazingaEntertainment (BZE) : AT&T:Entertainment
DailyPlanet (DIP) : NTT:Media
EvilInk (EVI) : Unilever:Misc
GringotsBank (GRB) : JPM:Finance
HammerTechnologies (HMT) : Microsoft:Tech
IlluminatiConsolidations (IIN) : Chevron:Finance
LexCorp (LEX) : GE:Tech
MonstersInc (MNC) : MCD:Misc
OlivanderWands (OWD) : UPS:Logistics
OscorpR&D (ORD) : Exxon:Tech
PalmerTechnologies (PLT) : Apple:Tech
PearsonHardmanConsultants (PHC) : FedEx:Consultants
SHIELD (SID) : Bank of America:Misc
Skynet (SKY) : Berkshire Hathaway:Consultants
StarkIndustries (STK) : IBM:Tech
StarLabs (STL) : Texas Instruments:Tech
UmbrellaCorp (UMB) : RIL:Tech
WalterWhiteInc (WWI) : Pfizer:Pharma
WayneEnterprises (WYE) : Google:Tech
XaviersSchools (XIR) : Dow Chemicals:Misc

'''
# DO NOT FUCK WITH THIS FOR FUCK'S SAKE!!!!!
# I GOT IT BY DOING SOME SHIT - YASH BONDE

RegressionCoeffAME = np.poly1d([7.27421285e-44, -1.62797460e-39, 1.63811861e-35,
                                -9.78989173e-32, 3.86639148e-28, -1.06209164e-24,
                                2.07922705e-21, -2.92177586e-18, 2.92709147e-15,
                                -2.04662043e-12, 9.60278776e-10, -2.83223280e-07,
                                4.70515919e-05, -3.55992862e-03, 7.04860129e-02,
                                5.87919174e+01])
RegressionCoeffAPM = np.poly1d([5.27284885e-45, -1.70638824e-40, 2.30800496e-36,
                                -1.77436276e-32, 8.75520985e-29, -2.94353959e-25,
                                6.94827081e-22, -1.16515282e-18, 1.38515121e-15,
                                -1.15031380e-12, 6.48428423e-10, -2.36734557e-07,
                                5.19034418e-05, -5.97535157e-03, 2.80945706e-01,
                                5.15744626e+01])
RegressionCoeffBSF = np.poly1d([-9.16473298e-45, 1.09239167e-40, 4.74143848e-39,
                                -7.55906769e-33, 6.36707873e-29, -2.80010860e-25,
                                7.79853682e-22, -1.46157925e-18, 1.87805747e-15,
                                -1.64777367e-12, 9.65953712e-10, -3.63803131e-07,
                                8.28528359e-05, -1.03321296e-02, 6.18960821e-01,
                                1.85751026e+01])
RegressionCoeffBJT = np.poly1d([1.03733171e-43, -2.55184009e-39, 2.83249362e-35,
                                -1.87458122e-31, 8.23380495e-28, -2.52794832e-24,
                                5.56472112e-21, -8.86369935e-18, 1.01830234e-14,
                                -8.31204970e-12, 4.68442292e-09, -1.73798059e-06,
                                3.92816985e-04, -4.77248222e-02, 2.60290823e+00,
                                8.34926095e+01])
RegressionCoeffBZE = np.poly1d([2.70819298e-44, -6.51435590e-40, 7.04151804e-36,
                                -4.51684575e-32, 1.91241997e-28, -5.62331932e-25,
                                1.17638369e-21, -1.76415737e-18, 1.88670993e-15,
                                -1.41483480e-12, 7.22581478e-10, -2.40737256e-07,
                                4.90777572e-05, -5.40334769e-03, 2.31728934e-01,
                                3.68897915e+01])
RegressionCoeffDIP = np.poly1d([-3.54653428e-44, 8.19316842e-40, -8.52746289e-36,
                                5.28214944e-32, -2.16699849e-28, 6.20039009e-25,
                                -1.26927244e-21, 1.87673467e-18, -1.99930896e-15,
                                1.51371388e-12, -7.93283631e-10, 2.75516240e-07,
                                -5.91768165e-05, 7.05773499e-03, -4.11014107e-01,
                                6.06168772e+01])
RegressionCoeffEVI = np.poly1d([7.37428794e-44, -1.75446694e-39, 1.88191678e-35,
                                -1.20217349e-31, 5.08861524e-28, -1.50236099e-24,
                                3.17112808e-21, -4.82456264e-18, 5.26537666e-15,
                                -4.05129661e-12, 2.12826888e-09, -7.24781977e-07,
                                1.47658386e-04, -1.60103231e-02, 7.97686204e-01,
                                4.19710487e+01])
RegressionCoeffGRB = np.poly1d([-1.10680322e-44, 2.22891677e-40, -1.96590346e-36,
                                9.93209799e-33, -3.14524203e-29, 6.36427813e-26,
                                -7.79811153e-23, 4.21544836e-20, 2.72004181e-17,
                                -7.10929726e-14, 6.33218359e-11, -3.23808428e-08,
                                9.83798590e-06, -1.49622759e-03, 6.62342270e-02,
                                3.86162648e+01])
RegressionCoeffHMT = np.poly1d([1.33369351e-43, -3.05551414e-39, 3.15302160e-35,
                                -1.93597386e-31, 7.87066489e-28, -2.23063149e-24,
                                4.51872516e-21, -6.60024036e-18, 6.92484488e-15,
                                -5.13814931e-12, 2.61960698e-09, -8.76234879e-07,
                                1.78729140e-04, -1.96186961e-02, 8.94689255e-01,
                                4.53672325e+01])
RegressionCoeffIIN = np.poly1d([-2.36588559e-44, 5.19001658e-40, -5.12464440e-36,
                                3.01335412e-32, -1.17774404e-28, 3.23927834e-25,
                                -6.48967661e-22, 9.69383718e-19, -1.09649618e-15,
                                9.43299260e-13, -6.07333076e-10, 2.79380971e-07,
                                -8.46972750e-05, 1.50548377e-02, -1.29030595e+00,
                                9.12237066e+01])
RegressionCoeffLEX = np.poly1d([4.89128036e-44, -1.17599057e-39, 1.27513471e-35,
                                -8.23485993e-32, 3.52306601e-28, -1.05064102e-24,
                                2.23759970e-21, -3.42970341e-18, 3.76458359e-15,
                                -2.91004035e-12, 1.53845496e-09, -5.32269287e-07,
                                1.13104977e-04, -1.34339817e-02, 7.55221460e-01,
                                5.71907264e+01])
RegressionCoeffMNC = np.poly1d([2.69950758e-44, -6.08134178e-40, 6.18478540e-36,
                                -3.75467660e-32, 1.51559372e-28, -4.28699744e-25,
                                8.72044206e-22, -1.28767362e-18, 1.37543869e-15,
                                -1.04646378e-12, 5.51364617e-10, -1.92846592e-07,
                                4.21892596e-05, -5.26104220e-03, 3.26497116e-01,
                                2.33694734e+01])
RegressionCoeffOWD = np.poly1d([2.32196014e-44, -5.89585059e-40, 6.75068203e-36,
                                -4.60592297e-32, 2.08456967e-28, -6.59173510e-25,
                                1.49415818e-21, -2.45129521e-18, 2.90403026e-15,
                                -2.45196430e-12, 1.43909553e-09, -5.63737464e-07,
                                1.37986504e-04, -1.88090854e-02, 1.12799791e+00,
                                6.03794510e+01])
RegressionCoeffORD = np.poly1d([1.70324853e-44, -3.90026577e-40, 4.01062436e-36,
                                -2.44570970e-32, 9.83458105e-29, -2.74133260e-25,
                                5.41504809e-22, -7.60424070e-19, 7.48540904e-16,
                                -4.98822400e-13, 2.10516318e-10, -4.94997953e-08,
                                4.84793033e-06, -9.10665243e-05, 7.08847422e-02,
                                4.57818765e+01])
RegressionCoeffPLT = np.poly1d([3.87481096e-43, -8.81659407e-39, 9.05789571e-35,
                                -5.55255077e-31, 2.26079896e-27, -6.43975877e-24,
                                1.31635263e-20, -1.94884504e-17, 2.08314820e-14,
                                -1.58435420e-11, 8.34378145e-09, -2.91455782e-06,
                                6.32153575e-04, -7.63984400e-02, 4.22097749e+00,
                                -1.49085081e+01])
RegressionCoeffPHC = np.poly1d([1.05486705e-44, -3.31792807e-40, 4.39445933e-36,
                                -3.32170186e-32, 1.61649371e-28, -5.37711930e-25,
                                1.26100426e-21, -2.11351002e-18, 2.53506446e-15,
                                -2.15629690e-12, 1.27501638e-09, -5.06348136e-07,
                                1.27103465e-04, -1.79782013e-02, 1.15782704e+00,
                                5.21852022e+01])
RegressionCoeffSID = np.poly1d([-1.24963374e-44, 2.28017704e-40, -1.79713983e-36,
                                8.15896303e-33, -2.51489009e-29, 6.48631633e-26,
                                -1.68194776e-22, 4.05881662e-19, -7.54019837e-16,
                                9.70283557e-13, -8.22862868e-10, 4.40978448e-07,
                                -1.41613082e-04, 2.52997026e-02, -2.19256276e+00,
                                2.55255526e+02])
RegressionCoeffSKY = np.poly1d([-2.43144975e-44, 3.71649476e-40, -1.81439470e-36,
                                -1.94216190e-33, 6.38234786e-29, -3.46860494e-25,
                                1.05265912e-21, -2.06547653e-18, 2.73320066e-15,
                                -2.45239127e-12, 1.46687810e-09, -5.63525165e-07,
                                1.30585495e-04, -1.63270231e-02, 8.84058275e-01,
                                7.41888005e+01])
RegressionCoeffSTK = np.poly1d([6.77694814e-44, -1.61799803e-39, 1.73917736e-35,
                                -1.11204508e-31, 4.70781019e-28, -1.38970176e-24,
                                2.93399075e-21, -4.47134673e-18, 4.90411196e-15,
                                -3.81680912e-12, 2.05432688e-09, -7.35081945e-07,
                                1.64950077e-04, -2.10428986e-02, 1.22178191e+00,
                                7.06249015e+01])
RegressionCoeffSTL = np.poly1d([1.61624067e-44, -4.02965980e-40, 4.51782021e-36,
                                -3.00860252e-32, 1.32396166e-28, -4.05158354e-25,
                                8.83409904e-22, -1.38293196e-18, 1.54601232e-15,
                                -1.21244502e-12, 6.45925216e-10, -2.22020175e-07,
                                4.53816293e-05, -4.86282265e-03, 2.53779094e-01,
                                1.84125842e+01])
RegressionCoeffUMB = np.poly1d([2.88443028e-43, -6.64436176e-39, 6.89488216e-35,
                                -4.25761304e-31, 1.74073719e-27, -4.96041476e-24,
                                1.00987747e-20, -1.48108170e-17, 1.55774805e-14,
                                -1.15557521e-11, 5.86562867e-09, -1.94174066e-06,
                                3.88715260e-04, -4.11077598e-02, 1.84901133e+00,
                                1.21772530e+01])
RegressionCoeffWWI = np.poly1d([-3.92916460e-44, 8.80917321e-40, -8.90880261e-36,
                                5.37548909e-32, -2.15726522e-28, 6.07675005e-25,
                                -1.23575265e-21, 1.83711007e-18, -1.99784756e-15,
                                1.57203830e-12, -8.73201863e-10, 3.27977437e-07,
                                -7.78199564e-05, 1.05359084e-02, -7.11168022e-01,
                                7.19808415e+01])
RegressionCoeffWYE = np.poly1d([1.95246245e-44, -4.85516544e-40, 5.49245097e-36,
                                -3.72373610e-32, 1.67884974e-28, -5.28474410e-25,
                                1.18780884e-21, -1.91824689e-18, 2.21230687e-15,
                                -1.78981862e-12, 9.84404652e-10, -3.50255412e-07,
                                7.45285143e-05, -8.35358865e-03, 4.65734993e-01,
                                6.63839532e+00])
RegressionCoeffXIR = np.poly1d([4.86035275e-44, -1.14197605e-39, 1.21077473e-35,
                                -7.65204180e-32, 3.20722032e-28, -9.38276093e-25,
                                1.96340341e-21, -2.96221622e-18, 3.20710723e-15,
                                -2.45154744e-12, 1.28626818e-09, -4.44442006e-07,
                                9.56586358e-05, -1.19259512e-02, 7.46923974e-01,
                                4.16772911e+01])

# This is the list of all the above data
RegressionCoeffList = [RegressionCoeffAME, RegressionCoeffAPM, RegressionCoeffBSF, RegressionCoeffBJT,
                       RegressionCoeffBZE,
                       RegressionCoeffDIP, RegressionCoeffEVI, RegressionCoeffGRB, RegressionCoeffHMT,
                       RegressionCoeffIIN,
                       RegressionCoeffLEX, RegressionCoeffMNC, RegressionCoeffOWD, RegressionCoeffORD,
                       RegressionCoeffPLT,
                       RegressionCoeffPHC, RegressionCoeffSID, RegressionCoeffSKY, RegressionCoeffSTK,
                       RegressionCoeffSTL,
                       RegressionCoeffUMB, RegressionCoeffWWI, RegressionCoeffWYE, RegressionCoeffXIR]

# YOU CAN SCREW THE CODE NOW

# Aditya wanted this in form of a function that he could call, so here it is

def SharePriceOutputWithoutNews(index, inputSharePrice, timePoint):

	print("Entering the function")

	# Choosing the regression values of the company on index
	# make sure that the index of comapnies in your code and Aditya's code is same, alphabetical order
	newSharePrice = float()
	companyRegressionValues = RegressionCoeffList[index]

	# Obtaining some basic data
	actualPrice = float(companyRegressionValues(timePoint))
	upperBound25 = actualPrice * 1.25
	upperBound15 = actualPrice * 1.15
	lowerBound15 = actualPrice * 0.85
	lowerBound25 = actualPrice * 0.75
	averageUpper = (actualPrice + upperBound15) / 2
	averageLower = (actualPrice + lowerBound15) / 2
	print(actualPrice)
	print(upperBound25)
	print(upperBound15)
	print(lowerBound15)
	print(lowerBound25)
	print(averageUpper)
	print(averageLower)
	print(inputSharePrice)

	# writing the cases for the bounding
	inputSharePrice = float(inputSharePrice)
	if inputSharePrice > upperBound15 and inputSharePrice < upperBound25:
		# case when sharePrice is between 15 to 25 zone upper
		# penalisation is 10% reduction in the price
		print(index, "Entered in loop condition1")
		amountOfPenalisation = 0.1
		amountOfPenalisationChange = 1 - amountOfPenalisation
		newSharePrice = amountOfPenalisationChange * inputSharePrice

	elif inputSharePrice < lowerBound15 and inputSharePrice > lowerBound25:
		# case when sharePrice is between 15 to 25 zone lower
		# penalisation is 10% increase in the share price
		print(index, "Entered in loop condition2")
		amountOfPenalisation = 0.1
		amountOfPenalisationChange = 1 + amountOfPenalisation
		newSharePrice = amountOfPenalisationChange * inputSharePrice

	elif inputSharePrice > upperBound25:
		# upper deviationRatio
		print(index, "Entered in loop condition3")
		deviationRatio = (inputSharePrice - averageUpper) / inputSharePrice
		amountOfPenalisationChange = 1 - deviationRatio
		newSharePrice = inputSharePrice * amountOfPenalisationChange

	elif inputSharePrice < lowerBound25:
		print(index, "Entered in loop condition4")
		deviationRatio = (inputSharePrice - averageLower) / inputSharePrice
		amountOfPenalisationChange = 1 - deviationRatio
		newSharePrice = amountOfPenalisationChange * inputSharePrice

	elif inputSharePrice >lowerBound15 and inputSharePrice < upperBound15:
		newSharePrice = inputSharePrice

	return newSharePrice