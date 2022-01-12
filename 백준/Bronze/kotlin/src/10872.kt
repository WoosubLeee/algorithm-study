fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    print(factorial(N))
}

fun factorial(n:Int): Int {
    if (n <= 1) return 1
    return n * factorial(n-1)
}