fun main() = with(System.`in`.bufferedReader()) {
    var N = readLine().toInt()
    var num = 665

    while (N > 0) {
        while (true) {
            num++
            if (num.toString().contains("666")) {
                N--
                break
            }
        }
    }

    print(num)
}