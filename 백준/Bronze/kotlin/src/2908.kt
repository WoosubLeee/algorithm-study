//fun main() = with(System.`in`.bufferedReader()) {
//    val nums = readLine().split(' ')
//    val A = nums[0]
//    val B = nums[1]
//
//    val larger: String
//    for (i in 2 downTo 0) {
//        if (A[i] > B[i]) {
//            larger = A
//        } else if (A[i] < B[i]) {
//            larger = B
//        } else {
//            continue
//        }
//        print("${larger[2]}${larger[1]}${larger[0]}")
//        break
//    }
//}

import java.util.StringTokenizer

fun main() = with(System.`in`.bufferedReader()) {
    val token = StringTokenizer(readLine().toString())

    val A = token.nextToken()
    val B = token.nextToken()

    val larger: String
    for (i in 2 downTo 0) {
        if (A[i] > B[i]) {
            larger = A
        } else if (A[i] < B[i]) {
            larger = B
        } else {
            continue
        }
        print("${larger[2]}${larger[1]}${larger[0]}")
        break
    }
}
