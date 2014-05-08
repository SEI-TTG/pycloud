/////////////////////////////////////////////////////////////////////////////////////
// Creates a modal dialog to show wait state for a process (no actual progress though).
/////////////////////////////////////////////////////////////////////////////////////
function WaitDialog (headerText) {
    // HTML for the modal dialog.
    var pleaseWaitDiv = '<div class="wait-dialog modal fade" id="pleaseWaitDialog" role="dialog" data-backdrop="static" data-keyboard="false"><div class="modal-dialog" id="pleaseWaitModal"><div class="modal-content"><div class="modal-header"><h3>'+headerText+'...</h3></div><div class="modal-body"><div class="progress progress-striped active"><div class="progress-bar" role="progressbar" style="width: 100%;"></div></div></div></div></div></div>';
    
    // Remove the modal once it's closed. NOTE: this is not working.
    $(document).on('hidden', '.wait-dialog', function () {
        $(this).remove();
    });    
    
    // Functions to show and hide the dialog.
    return {
        show: function() {
            $('body').append(pleaseWaitDiv);
            $('.wait-dialog').show();
            $('.wait-dialog').modal();
        },
        hide: function () {
            $('.wait-dialog').modal('hide');
        },
    };
}

/////////////////////////////////////////////////////////////////////////////////////
// Creates a notification to inform the user of an event.
/////////////////////////////////////////////////////////////////////////////////////
function Alert(level, message, alertContainer) {
    // Template for the alert message.
    var alertDiv = $('<div id="alert-div" style="position: fixed; top: 55px; display: block; width=50%; margin-left: auto; margin-right: auto;"><div class="alert alert-dismissable fade in alert-'+level+'" id="alert-element"><button type="button" class="close" data-dismiss="alert" aria-hidden="true">&times;</button><div id="alert-text">'+message+'</div></div></div>');

    // Functions.
    return {
        show: function() {
            // Set the container for the alert.
            if(alertContainer == null)
            {
                alertContainer =  $('#navbar-container');
            }
            
            // Show the alert.
           alertContainer.append(alertDiv);
            
            // Add timer to auto-close the alert after some time.
            alertElement = $('#alert-element');
            alertDiv.fadeIn(200, function () {
                setTimeout(function () {
                    alertElement.alert('close');
                    alertElement.parent().remove();
                }, 5000);
            });
        },
    };
}

/////////////////////////////////////////////////////////////////////////////////////
// Function to show a notification and log it in the console.
/////////////////////////////////////////////////////////////////////////////////////
function showAndLogSuccessMessage(message, parent)
{
    // Default value.
    if(typeof(parent)==='undefined') parent = null;
    
    // Log and show alert.
    window.console && console.log(message);
    var alertBox = Alert('success', message, parent);
    alertBox.show();
}

/////////////////////////////////////////////////////////////////////////////////////
// Function to show a notification and log it in the console.
/////////////////////////////////////////////////////////////////////////////////////
function showAndLogErrorMessage(message, status, errorThrown, parent)
{
    // Default values.
    if(typeof(status)==='undefined') status = '';
    if(typeof(errorThrown)==='undefined') errorThrown = '';
    if(typeof(parent)==='undefined') parent = null;
        
    // Log and show alert.        
    window.console && console.log(message, status, errorThrown);
    var alertBox = Alert('danger', message, parent);
    alertBox.show();
}

/////////////////////////////////////////////////////////////////////////////////////
// Function to check if an Ajax call was successful.
/////////////////////////////////////////////////////////////////////////////////////
function ajaxCallWasSuccessful(response)
{
    // Parse the response into a JSON structure.
    var jsonData = JSON.stringify(response);
    //console.log(jsonData);
    var parsedJsonData = $.parseJSON(jsonData);
    
    // Check if we got an error.
    if(parsedJsonData.hasOwnProperty('STATUS') && parsedJsonData.STATUS=='NOT OK')
    {
        return false;
    }
    else
    {
        return true;
    }
}