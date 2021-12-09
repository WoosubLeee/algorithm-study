import java.util.Scanner

fun main() {
    val sc: Scanner = Scanner(System.`in`)
    
    val n = sc.nextInt()

    var sum = 0
    for (i in 1..n) {
        sum += i
    }
    print(sum)
}