import java.io.BufferedWriter
import java.io.OutputStreamWriter

fun combine(nums: MutableList<Int>, start: Int, N: Int, M: Int, bw: BufferedWriter) {
    if (nums.size == M) {
        bw.write("${nums.joinToString(" ")}\n")
    } else {
        for (i in start..N-(M-nums.size-1)) {
            nums.add(i)
            combine(nums, i+1, N, M, bw)
            nums.remove(i)
        }
    }
}

fun main() = with(System.`in`.bufferedReader()) {
    val bw = BufferedWriter(OutputStreamWriter(System.out))

    val input = readLine().split(' ').map { x -> x.toInt() }
    val N = input[0]
    val M = input[1]

    val nums = mutableListOf<Int>()

    combine(nums, 1, N, M, bw)
    bw.flush()
}