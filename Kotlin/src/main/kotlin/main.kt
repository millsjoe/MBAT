import kotlin.Array as Array
import com.google.gson.Gson
import java.io.File

fun main(args: Array<String>) {
    val arraySize = args[0].toInt()
    val counter = (arraySize*0.4) * (arraySize*0.1)
    val gson = Gson()
    val array = Array(arraySize) { IntArray(arraySize) }
    Surface(array)
    val initial = Cell(array).randomCell()

    val playingBoard = Diffuse(array,initial,counter.toInt())

    val theArray: String = gson.toJson(Model(playingBoard.surface))

    val fileToWriteTo = "../JSON/Kotlin_" + arraySize + ".json"
    File(fileToWriteTo).writeText((theArray))


}

