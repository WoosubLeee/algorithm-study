fun main() = with(System.`in`.bufferedReader()) {
    var result = 0
    var isMinus= false

    var temp = 0
    for (i in readLine()) {
        if (i in "+-") {
            if (isMinus) {
                temp *= -1
            }
            result += temp
            temp = 0
            if (i == '-') isMinus = true
        } else {
            temp *= 10
            temp += Character.getNumericValue(i)
        }
    }
    if (isMinus) {
        temp *= -1
    }
    result += temp

    print(result)
}