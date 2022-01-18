fun main() = with(System.`in`.bufferedReader()) {
    var N = readLine().toInt()

    var num = 0
    while (N > 0) {
        num += 1
        if ("666" in num.toString()) {
            N -= 1
        }
    }
    print(num)
}