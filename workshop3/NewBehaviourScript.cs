using System.Collections;
using System.Collections.Generic;
using UnityEngine;
using UnityEngine.Networking;
using SimpleJSON;

public class GoogleSheetsData : MonoBehaviour
{
    public string apiKey = "AIzaSyAyNYGYDco1oFhD0VheKc3jgb-hi-l0yQY"; 
    public string sheetId = "1_RmpdxtCpZq1AVZgVg7kyt0D7LEFrzSdpouCPSJaBaE";
    public string sheetName = "BigDigital GameLab";

    private Dictionary<string, float> dataSet = new Dictionary<string, float>();

    void Start()
    {
        StartCoroutine(DownloadGoogleSheetData());
    }

    IEnumerator DownloadGoogleSheetData()
    {
        // Формируем URL для запроса
        string url = $"https://sheets.googleapis.com/v4/spreadsheets/{sheetId}/values/{sheetName}?key={apiKey}";

        // Отправляем запрос
        UnityWebRequest request = UnityWebRequest.Get(url);
        yield return request.SendWebRequest();

        if (request.result == UnityWebRequest.Result.Success)
        {
            // Получаем и выводим ответ
            var rawResponse = request.downloadHandler.text;
            Debug.Log("Response: " + rawResponse);

            // Парсим JSON
            var json = JSON.Parse(rawResponse);

            // Извлекаем значения
            var values = json["values"];
            for (int i = 0; i < values.Count; i++)
            {
                string row = "";
                for (int j = 0; j < values[i].Count; j++)
                {
                    row += values[i][j] + " ";
                }
                Debug.Log($"Row {i + 1}: {row}");
            }
        }
        else
        {
            Debug.LogError($"Error: {request.error}");
        }
    }
}