import kotlin.math.floor

// 🔶 Меню программы
fun startApp() {
    println()
    println(" /\\_/\\  \n( o.o )\n > ^ < ")
    println()
}

// 🔶 Расчёт комиссии одного чека
fun getCommForReceipt(receipt: Int): Int = when {
    receipt < 80 -> 0
    receipt < 100 -> 1
    receipt < 140 -> 2
    receipt < 220 -> 3
    receipt < 240 -> 4
    receipt < 320 -> 5
    receipt < 340 -> 6
    receipt < 380 -> 7
    receipt < 460 -> 8
    receipt < 600 -> 9
    else -> 15  // на случай, если отдельный чек >= 600
}

// 🔶 Комиссия с иностранцев: 3% от суммы, округлённое
fun calcForeignComm(total: Int): Int {
    val foreignComm = total * 0.03
    return floor(foreignComm + 0.5).toInt()
}

// Чтение чисел, разделённых пробелами
fun readReceipts(): List<Int> =
    readln().trim().split(Regex("\\s+")).filter { it.isNotEmpty() }.map { it.toInt() }

fun main() {
    startApp()

    print("🔅 Введите суммы чеков через пробел: ")
    val receipts = readReceipts()
    val totalSum = receipts.sum()
    var totalComm = 0
    var addBlocks = 0

    if (totalSum < 600) {  // считаем комиссию отдельно для каждого чека
        println()
        for (i in receipts.indices) {
            val comm = getCommForReceipt(receipts[i])
            totalComm += comm
            println("🔹 Чек ${i + 1}: ${receipts[i]} → комиссия \$$comm")
        }
    } else {  // считаем по общему правилу >= 600
        totalComm = 15
        val extra = totalSum - 600

        if (extra > 0) {
            addBlocks = extra / 140  // количество блоков по 140
            totalComm += addBlocks * 3
        }
    }

    println()
    println("💲 Общая сумма: \$$totalSum")
    if (totalSum >= 600) {
        println("💲 Общая комиссия: \$15 + \$3 x $addBlocks → \$$totalComm")
    } else {
        println("💲 Общая комиссия: \$$totalComm")
    }

    println()
    print("🔅 Есть комиссия для иностранцев? y/n ")
    val foreign = readln()
    if (foreign == "y") {
        println()
        print("🔅 Введите суммы чеков через пробел: ")
        val receiptsF = readReceipts()
        val totalSumF = receiptsF.sum()
        val totalCommF = calcForeignComm(totalSumF)
        println()
        println("💲 Общая сумма: \$$totalSumF")
        println("💲 Комиссия (3% от суммы): \$$totalCommF")
    }
}