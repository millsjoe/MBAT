import kotlin.Array as Array
import com.google.gson.Gson
import java.io.File

fun main(args: Array<String>) {
    val arraySize = args[0].toInt()
    val counter = args[1].toInt()
    val gson = Gson()
    val array = Array(arraySize) { IntArray(arraySize) }
    Surface(array)
    val initial = Cell(array).randomCell()

    val playingBoard = Diffuse(array,initial,counter)

    val theArray: String = gson.toJson(Model(playingBoard.finalArray))


    File("../Python/Kotlin.json").writeText((theArray))


}

