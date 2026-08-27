class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:
            return "Zero"

        ones = [
            "", "One", "Two", "Three", "Four",
            "Five", "Six", "Seven", "Eight", "Nine",
            "Ten", "Eleven", "Twelve", "Thirteen",
            "Fourteen", "Fifteen", "Sixteen", "Seventeen",
            "Eighteen", "Nineteen"
        ]

        tens = [
            "", "", "Twenty", "Thirty", "Forty",
            "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"
        ]

        def convert(n):
            result = []

            if n >= 100:
                result.append(ones[n // 100])
                result.append("Hundred")
                n %= 100

            if n >= 20:
                result.append(tens[n // 10])
                n %= 10

            if n > 0:
                result.append(ones[n])

            return " ".join(result)

        result = []

        if num >= 1_000_000_000:
            result.append(convert(num // 1_000_000_000))
            result.append("Billion")
            num %= 1_000_000_000

        if num >= 1_000_000:
            result.append(convert(num // 1_000_000))
            result.append("Million")
            num %= 1_000_000

        if num >= 1000:
            result.append(convert(num // 1000))
            result.append("Thousand")
            num %= 1000

        if num > 0:
            result.append(convert(num))

        return " ".join(result)