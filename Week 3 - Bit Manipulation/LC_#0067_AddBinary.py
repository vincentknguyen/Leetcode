{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae304503",
   "metadata": {},
   "outputs": [],
   "source": [
    "class Solution(object):\n",
    "    def addBinary(self, a, b):        \n",
    "        #given 2 binary STRINGS\n",
    "        \n",
    "        result = \"\"\n",
    "        carry = 0\n",
    "        \n",
    "        a = list(a)\n",
    "        b = list(b)\n",
    "        \n",
    "        while a or b or (carry == 1):\n",
    "            \n",
    "            if a:\n",
    "                carry += int(a.pop())\n",
    "            if b:\n",
    "                carry += int(b.pop())\n",
    "            \n",
    "            result += str(carry % 2)\n",
    "            \n",
    "            carry = carry // 2\n",
    "        \n",
    "        return result[::-1]\n",
    "            "
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.8.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
