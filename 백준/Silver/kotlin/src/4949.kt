import java.util.*

fun main() = with(System.`in`.bufferedReader()) {
    val result = mutableListOf<String>()

    while (true) {
        val line = readLine()
        if (line == ".")  break

        val stack = Stack<Char>()
        var wrong = "yes"
        for (i in line) {
            if (i in arrayOf('(', '['))  stack.push(i)
            else if (i in arrayOf(')', ']')) {
                if (stack.isEmpty()) {
                    wrong = "no"
                    break
                }
                val top = stack.pop()
                if ((i == ')' && top != '(') || (i == ']' && top != '[')) {
                    wrong = "no"
                    break
                }
            }
        }
        if (stack.isNotEmpty()) wrong = "no"

        result.add(wrong)
    }
    print(result.joinToString("\n"))
}