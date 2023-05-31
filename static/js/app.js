let openButtons = document.querySelectorAll('.open-modal'),
closeButtons = document.querySelectorAll('.close'),
modals = document.querySelectorAll('.modal'),
select = document.querySelector('[name="semester"]'),
excelTemplateUrl = document.querySelector('#template-url')
,input = document.querySelector('#user-id')

let onSelectChange = () => {
    excelTemplateUrl.href = `static/marks-template/0${select.value}-semester.xlsx`
}

select.addEventListener('change', onSelectChange)


for (let x of openButtons) {
    x.addEventListener('click', (e) => {
        for (let y of modals) {
            if (x.getAttribute('data-modal-id') == y.getAttribute('data-modal-name')) {
                
                input.value = x.getAttribute('data-people-id')

                y.classList.remove('d-none')
                y.classList.add('modal-anim')
                y.querySelector('.modal-content').classList.add('modal-content-anim')

                select.value = '1'
                onSelectChange()
            }
        }
    })
}

for (let z of closeButtons) {
    z.addEventListener('click', (e) => {
        for (let w of modals) {
            if (z.getAttribute('data-modal-id') == w.getAttribute('data-modal-name')) {
                w.classList.add('d-none')
                w.classList.remove('modal-anim')
            }
        }
    })
}



