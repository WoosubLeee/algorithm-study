import java.util.*
import kotlin.math.sqrt

fun main() = with(System.`in`.bufferedReader()) {
    for (t in 1..readLine().toInt()) {
        var token = StringTokenizer(readLine().toString())
        var x = token.nextToken().toInt()
        var y = token.nextToken().toInt()

        var distance = y - x

//        var moved = 0
//        var inOneMove = 0
//        while (distance > 0) {
//            inOneMove += 1
//
//            distance -= inOneMove*2
//            moved += 2
//            if (-distance >= inOneMove) {
//                moved -=1
//            }
//        }
//        println(moved)

        var max = sqrt(distance.toDouble()).toInt()

        var count: Int
        if (distance == max*max) {
            count = 2*max - 1
        } else if (distance <= max*(max+1)) {
            count = 2*max
        } else {
            count = 2*max + 1
        }
        println(count)
    }
}