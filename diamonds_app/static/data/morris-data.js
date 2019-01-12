$(function() {

    Morris.Area({
        element: 'morris-area-chart',
        data: [{
            carat: 0.5,
            price: 1,
            
        }, {
            carat: 0.6,
            price: 2,
            
        }, {
            carat: 0.7,
            price: 3,
            
        }, {
            carat: '2012 Q1',
            price: 4,
            
        }, {
            carat: '2012 Q2',
            price: 5,
            
        }],
        xkey: 'carat',
        ykeys: 'price',
        labels: ['price'],
        pointSize: 2,
        hideHover: 'auto',
        resize: true
    });

    
});
