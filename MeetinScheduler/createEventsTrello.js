// This file reads in daily events from a file and pushes them to Trello

var Trello = require("node-trello");
var async  = require("async");
var t = new Trello("16f60be4c670af4fc8857141515bdda3", "712c22653001f7a637be02757e7926a8051183e21e51d560e70a74f67506f101");

// A nice print function
function nPrint(str) {
  console.log(JSON.stringify(str, null, 4));
}

function getCardFromID(cardID, callback) {
  t.get('/1/cards/' + cardID,
        {actions: "all"},
        function(err, card) {
    if (err) throw err;
    var actionsLen = card.actions.length;
    sub_total = 0;
    var myHash = {};
    for (var i = 0; i < actionsLen; ++i) {
      if (card.actions[i].data.listAfter != undefined) {
        var listAfter = JSON.stringify(card.actions[i].data.listAfter, null, 4);
        if (listAfter.indexOf("Done") != -1) {
	  actionTime = new  Date(Date.parse(card.actions[i].date) - 4*60*60*1000);
	  actionTimeStr = actionTime.toISOString();
          updateHash(myHash, 
                     actionTimeStr.split("T")[0],  
                     parseFloat(card.name.split(" ")[0]));
	}
      }
    }
    accum(myHash);
    callback();
  });
}

var total = 0;
var totHash = {};


var success = function(successMsg) {
  console.log("success: " + successMsg);
};

var error = function(errorMsg) {
  console.log("error: " + errorMsg);
};

// Reads in meetings.txt and adds all events to list listID
function addEventsToList(listID) {
  fs = require('fs')
  fs.readFile('Documents/PracticeCode/MeetinScheduler/meetings.txt', 'utf8', function (err,data) {
    if (err) {
      return console.log(err);
    }
    meetings = data.split("\n");
    meetingsLen = meetings.length;
    for (var i = 0; i < meetingsLen -1; ++i) {
      mInfo = meetings[i].split(/[:-]/);
      mLength = (parseFloat(mInfo[2]) * 60 + parseFloat(mInfo[3]) - 
                 (parseFloat(mInfo[0]) * 60 + parseFloat(mInfo[1]))) / 60

      var newCard = {
        name: mLength + mInfo[4],
        desc: "",
        pos: "top",
        due: "null",
        idList: listID
      };
      t.post('1/cards/', newCard, success, error);
    }
  });
}


// We open the Master's work board, and add all events from meetings.txt to
// the board in the "Other" List
t.get('/1/members/me/boards', {lists: "open"}, 
      function(err, data) {
  if (err) throw err;
  var dataLen = data.length;
  for (var i = 0; i < dataLen; ++i) {
    if (data[i].name == "Master's Work") {
      var listsLen = data[i].lists.length;
      for (var j = 0; j < listsLen; ++j) {
        var listStr = JSON.stringify(data[i].lists[j], null, 4);
        if (listStr.indexOf("Other") != -1) {
          listID = data[i].lists[j].id;
          addEventsToList(listID);
	}        
      }
    }
  }
});

function printHash(myHash) {
  retVals = []
  for (var item in myHash) {
    retVals.push(item + ": " + myHash[item]);
  }
  retVals.sort()
  for (var item in retVals) {
    nPrint(retVals[item]);
  }

}

