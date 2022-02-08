fun main() = with(System.`in`.bufferedReader()) {
    val N = readLine().toInt()
    val confs = mutableListOf<List<Int>>()
    for (i in 1..N) {
        confs.add(readLine().split(' ').map { num -> num.toInt() })
    }

    confs.sortWith(compareBy({it[1]}, {it[0]}))

    var count = 0
    var end = 0
    for (conf in confs) {
        if (conf[0] >= end) {
            count++
            end = conf[1]
        }
    }
    print(count)
}