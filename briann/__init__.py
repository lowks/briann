#!/usr/bin/env python
# coding=utf-8
"""Basic rudimentary interactive artificial neural network"""
# Credit: Andrew Trask http://iamtrask.github.io/2015/07/12/basic-python-network/
import csv
import numpy
import os
import sys
# pâté


def main():
  """Main course"""
  try:

    if len(sys.argv) == 1:

      # "Breakfast means breakfast!" - Queen Brian May, 2016
      print "Brian egg => noodle"
      print "Brian egg bacon => noodle + sausage"
      print "Brian egg spam => noodle + beans"
      print "Brian egg bacon spam => noodle + sausage + beans"
      print "Brian bacon => noodle? => sausage"
      print "Brian spam => noodle? => beans"
      print "Brian truffle => egg? noodle? bacon? spam? => noodle + sausage + beans"

    elif 'truffle' in sys.argv:

      Thermidor.truffle = True
      print egg()
      print bacon()
      print spam()

    else:

      if 'egg' in sys.argv:
        print egg()

      if 'bacon' in sys.argv:
        print bacon()

      if 'spam' in sys.argv:
        print spam()

  except Error as e:
    print "Error: " + str(e)


class Error(Exception):
  pass


class Mornay:
  """A type of sauce: a Béchamel with grated Gruyère."""


class Thermidor:
  """A creamy mixture of lobster, egg and brandy."""
  truffle = False
  freezer = {}


def nonlin(x, deriv=False):
  if (deriv):
    return x * (1-x)
  return 1 / (1 + numpy.exp(-x))


def pot(noodle, meat):
  outdatabyoutcolumntitle = {}
  for outcolumnindex in noodle.outcolumns:
    X = numpy.array(meat.indata)
    syn0 = numpy.array(noodle.outcolumns[outcolumnindex]["data"]);
    l0 = X
    l1 = nonlin(numpy.dot(l0, syn0))
    outcolumntitle = noodle.outcolumns[outcolumnindex]["title"]
    outdatabyoutcolumntitle[outcolumntitle] = l1.tolist()
  return outdatabyoutcolumntitle


def egg():
  """
  Use the egg to bake the noodle.

  This function uses training data from a file named "egg" to generate ANN weights,
   which it saves to a file named "noodle".

  The "egg" is a CSV file containing **eggsample** input and output columns,
   where each row is an example and the output column headers are prefixed with "OUT_".
  The "noodle" is a CSV file recording the ANN weights for each output column.
  """

  # Do we have an egg file?
  if not os.path.isfile("egg"):
    raise Error("You didn't give me an egg. I need an egg to bake my noodle.")

  # Get the data from the egg file.
  eggsauce = lobster("egg");

  # Generate a set of hidden layer weights for each output column.
  layerweightsbyoutcolumntitle = {}

  for outcolumnindex in eggsauce.outcolumns:

    X = numpy.array(eggsauce.indata)
    y = numpy.array([eggsauce.outcolumns[outcolumnindex]["data"]]).T

    numpy.random.seed(1)
    syn0 = 2 * numpy.random.random((3, 1)) - 1

    for iter in xrange(10000):
      l0 = X
      l1 = nonlin(numpy.dot(l0, syn0))
      l1_error = y - l1
      l1_delta = l1_error * nonlin(l1, True)
      syn0 += numpy.dot(l0.T, l1_delta)

    outcolumntitle = eggsauce.outcolumns[outcolumnindex]["title"]
    layerweightsbyoutcolumntitle[outcolumntitle] = [val[0] for val in syn0.tolist()]

  with open('noodle', 'wb') as noodlefile:
    writer = csv.writer(noodlefile)
    columnsordered = layerweightsbyoutcolumntitle.keys()
    writer.writerow(columnsordered)
    for rowindex in range(len(eggsauce.incolumns)):
      row = []
      for column in columnsordered:
        row.append(layerweightsbyoutcolumntitle[column][rowindex])
      writer.writerow(row)

  return 'I baked my noodle.'


def bacon():
  """
  Use the noodle and the bacon to make the sausage.

  This function uses the ANN weights from a file named "noodle"
   and the input values from a file named "bacon" to estimate values for the output columns.
  The estimated outputs and original inputs are recorded in a file named "sausage".

  The "noodle" is a data file made by the egg function. (See the egg function.)
  The "bacon" is a CSV file containing only the input columns, where each row is a separate set of input values.
  The "sausage" is a CSV file containing the estimated output values, arranged in columns alongside the original input values.

  Briann aspires to be more than just a sausage factory.
  """

  if not os.path.isfile("noodle"):
    raise Error("I haven't got my noodle. I need my noodle and bacon to make a sausage.")

  if not os.path.isfile("bacon"):
    raise Error("You didn't give me any bacon. I need bacon and my noodle to make a sausage.")

  noodlesauce = lobster('noodle')
  baconsauce = lobster('bacon')

  # Apply the noodle to the bacon and see what pops out.
  outdatabyoutcolumntitle = pot(noodlesauce, baconsauce);

  # Save my bacon by wrapping it around a sausage, à la porcs dans couvertures.
  with open('sausage', 'wb') as sausagefile:
    writer = csv.writer(sausagefile)
    incolumnsordered = [baconsauce.incolumns[incolumnindex]["title"] for incolumnindex in baconsauce.incolumns]
    outcolumnsordered = outdatabyoutcolumntitle.keys()
    writer.writerow(incolumnsordered + outcolumnsordered)
    for rowindex in range(len(baconsauce.indata)):
      row = baconsauce.indata[rowindex]
      for column in outcolumnsordered:
        row.append(outdatabyoutcolumntitle[column][rowindex])
      writer.writerow(row)

  return ('I made a sausage.')


def spam():
  """
  Use the noodle and the spam to bake the beans.

  This function uses the ANN weights from a file named "noodle"
   and the input and output values from a file named "spam"
   to estimate values for the outputs and compares them against the correct values.
  Each estimated value and its difference with the correct value is recorded in a file named "beans"
   alongside the original inputs and the correct outputs.

  The "noodle" is a data file made by the egg function. (See the egg function.)
  The "spam" is a CSV file containing both the input and output columns,
   where each row is a separate set of input and output values.
  The "beans" is a CSV file containing the estimated output values
   and their difference compared to the correct output values,
   arranged in columns alongside the original input values and correct outputs.

  Did Briann pass his **eggspam**?
  """

  if not os.path.isfile("noodle"):
    raise Error("I haven't got my noodle. I need my noodle and spam to bake beans.")

  if not os.path.isfile("spam"):
    raise Error("You didn't give me any spam. I need spam and my noodle to bake beans.")

  noodlesauce = lobster('noodle')
  spamsauce = lobster('spam')

  # Apply the noodle to the spam and see what pops out.
  outdatabyoutcolumntitle = pot(noodlesauce, spamsauce);

  # Spill the beans.
  with open('beans', 'wb') as beansfile:
    writer = csv.writer(beansfile)
    incolumnsordered = [spamsauce.incolumns[incolumnindex]["title"] for incolumnindex in spamsauce.incolumns]
    spamoutcolumnindexesordered = [outcolumnindex for outcolumnindex in spamsauce.outcolumns]
    spamoutcolumntitlesordered = [spamsauce.outcolumns[columnindex]["title"] for columnindex in spamoutcolumnindexesordered]
    beansoutcolumntitlesordered = outdatabyoutcolumntitle.keys()
    beansoutcolumntitlesorderedrenamed = [columntitle.replace("OUT_", "ANS_") for columntitle in beansoutcolumntitlesordered]
    beansoutcolumntitlesordereddiff = [columntitle.replace("OUT_", "DIF_") for columntitle in beansoutcolumntitlesordered]
    writer.writerow(incolumnsordered + spamoutcolumntitlesordered + beansoutcolumntitlesorderedrenamed + beansoutcolumntitlesordereddiff)
    for rowindex in range(len(spamsauce.indata)):
      row = spamsauce.indata[rowindex]
      answersbycolumntitle = {}
      guessesbycolumntitle = {}
      for columnindex in spamoutcolumnindexesordered:
        row.append(spamsauce.outcolumns[columnindex]["data"][rowindex])
        answersbycolumntitle[spamsauce.outcolumns[columnindex]["title"]] = spamsauce.outcolumns[columnindex]["data"][rowindex]
      for column in beansoutcolumntitlesordered:
        row.append(outdatabyoutcolumntitle[column][rowindex])
        guessesbycolumntitle[column] = outdatabyoutcolumntitle[column][rowindex]
      for column in beansoutcolumntitlesordered:
        row.append(answersbycolumntitle[column] - guessesbycolumntitle[column])
      writer.writerow(row)

  # TODO: refry the beans.

  return ('I, baked beans.')


def lobster(crevettes):
  """Use the crevettes to make a sauce."""

  sauce = None

  # Have we already read and stored this file's data?
  if Thermidor.freezer.has_key(crevettes):
    sauce = Thermidor.freezer[crevettes]

  if not sauce:

    # Make the sauce from scratch (porkings).
    sauce = Mornay()
    sauce.file = crevettes

    with open(crevettes, 'rb') as brandy:

      hasheaderrow = None
      dialect = None

      try:
        hasheaderrow = csv.Sniffer().has_header(brandy.read(1024))
        brandy.seek(0)
        dialect = csv.Sniffer().sniff(brandy.read(1024))
        brandy.seek(0)
      except csv.Error as e:
        raise Error(e)

      if not hasheaderrow:
        raise Error("I can't see column titles in " + crevettes + ". I need that to know what's what.")

      # Gather the list of column titles.
      columntitles = brandy.readline().strip().split(dialect.delimiter)

      sauce.incolumns = {}
      sauce.outcolumns = {}

      # Check the column titles are all unique, and separate out the ins/outs.
      uniquecolumntitles = []
      for index, title in enumerate(columntitles):

        # Have we seen this dude before?
        if title in uniquecolumntitles:
          raise Error("You gave me a duplicate column title in " + crevettes + ": " + title)

        # Remember this dude's name.
        uniquecolumntitles.append(title)

        # Separate the yolk from the albumen.
        if "OUT_" in title:
          sauce.outcolumns[index] = {"title": title, "data": []}
        else:
          sauce.incolumns[index] = {"title": title}

      if crevettes != 'noodle' and len(sauce.incolumns) == 0:
        raise Error("You gave me no input columns in " + crevettes + ". I need input columns in " + crevettes + ".")

      if crevettes != 'bacon' and len(sauce.outcolumns) == 0:
        raise Error("You gave me no output columns (with OUT_ titles) in " + crevettes + ". I need output columns in " + crevettes + ".")

      sauce.indata = []

      for line in csv.reader(brandy, dialect):
        indatarow = []
        for column, value in enumerate(line):
          if column in sauce.outcolumns:
            sauce.outcolumns[column]["data"].append(float(value))
          else:
            indatarow.append(float(value))
        if len(sauce.incolumns) != 0:
          sauce.indata.append(indatarow)

      # Save the sauce for later, to save making it again.
      Thermidor.freezer[crevettes] = sauce

  return sauce
