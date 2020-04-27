import kotlin.Array as Array
import com.google.gson.Gson
import java.io.File

/**
 * 
 *   Main takes the environment size and calls on other classes
 *   to begin the application 
 *   
 *   @param args Command line arguments
 */

fun main(args: Array<String>) {
    val arraySize = args[0].toInt()
    val counter = (arraySize*0.2) * (arraySize*0.2)

    val gson = Gson()
    val array = Array(arraySize) { IntArray(arraySize) }
    
    val startTime = System.currentTimeMillis()
    
    Surface(array)
    val initial = Cell(array).randomCell()

    val playingBoard = Diffuse(array,initial,counter.toInt())
    
    val endTime = System.currentTimeMillis()
    val difference = (endTime - startTime) 
    val timeTaken = difference.toFloat() / 1000 // Change to seconds

    val theArray: String = gson.toJson(Model(playingBoard.surface))

    val fileToWriteTo = "../JSON/Kotlin_" + arraySize + ".json"
    File(fileToWriteTo).writeText((theArray))

    val resultsToWriteTo = "../Results/Kotlin_results.csv"
    File(resultsToWriteTo).appendText("Kotlin," + arraySize + ",%.5f".format(timeTaken) + "\n")
}

