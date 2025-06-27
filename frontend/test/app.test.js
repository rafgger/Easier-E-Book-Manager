const assert = chai.assert;

describe('E-Book Overview', function() {
    it('renders book cards', function() {
        const books = [
            { ISBN: '1', title: 'A', author: 'B', year: 2000, cover: 'img.jpg' },
            { ISBN: '2', title: 'C', author: 'D', year: 2001, cover: 'img2.jpg' }
        ];
        renderBooks(books);
        const cards = document.querySelectorAll('.book-card');
        assert.equal(cards.length, 2);
        assert.include(cards[0].innerHTML, 'A');
        assert.include(cards[1].innerHTML, 'C');
    });
});

describe('E-Book Detail', function() {
    it('renders book detail', function() {
        const book = { ISBN: '1', title: 'A', author: 'B', year: 2000, publisher: 'P', cover: 'img.jpg' };
        renderBookDetail(book);
        assert.include(bookDetail.innerHTML, 'A');
        assert.include(bookDetail.innerHTML, 'P');
    });
});
