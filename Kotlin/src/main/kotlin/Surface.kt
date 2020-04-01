import kotlin.math.roundToInt

class Surface(private val surface: Array<IntArray>) {
    private val maxAmount: Int = surface.size - 1

    init {
        this.markABorder()
        this.centralCell()
    }

    private fun markABorder() {

        for (i in 0..maxAmount) {
            surface[0][i] = 2
            surface[maxAmount][i] = 2
            surface[i][0] = 2
            surface[i][maxAmount] = 2
            surface[maxAmount][maxAmount] = 2
        }
    }
    private fun centralCell() {
        val central = surface.size.toFloat() / 2
        surface[central.roundToInt()][central.roundToInt()] = 1
    }



}