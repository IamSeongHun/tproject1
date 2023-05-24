function toggleTable() {
    var tableContainer = document.getElementById('tableContainer');
    var toggleButton = document.getElementById('toggleTableBtn');
  
    if (tableContainer.style.display === 'none') {
      tableContainer.style.display = 'block';
      toggleButton.innerHTML = '테이블 가리기';
    } else {
      tableContainer.style.display = 'none';
      toggleButton.innerHTML = '테이블 보이기';
    }
  }
  
  // 테이블 생성 함수
  function createTable(data) {
    var tableContent = document.getElementById('tableContent');
    var tableHTML = '<table><tr><th>순번</th><th>소속</th><th>학번</th><th>학생이름</th></tr>';
  
    for (var i = 0; i < data.length; i++) {
      tableHTML += '<tr>';
      for (var j = 0; j < data[i].length; j++) {
        tableHTML += '<td>' + data[i][j] + '</td>';
      }
      tableHTML += '</tr>';
    }
  
    tableHTML += '</table>';
    tableContent.innerHTML = tableHTML;
  }
  
  // 데이터베이스에서 가져온 데이터로 테이블 생성
  createTable(result2);
  