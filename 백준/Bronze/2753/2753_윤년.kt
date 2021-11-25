import java.util.Scanner

fun main() {
    val sc: Scanner = Scanner(System.`in`)
    var year = sc.nextInt()

    if (year % 4 != 0 || (year % 100 == 0 && year % 400 != 0)) {
        print(0)    
    } else {
        print(1)
    }
}